import streamlit as st
from streamlit_timeline import st_timeline

from datetime import datetime


def short_role(start, end, threshold_days):
    s = datetime.strptime(start, "%Y-%m-%d")
    e = datetime.strptime(end, "%Y-%m-%d")
    return (e - s).days < threshold_days


def convert_to_timeline_items(experience_dict):
    timeline_items = []

    for id_, data in experience_dict.items():
        content = data["company"]  # Only show company name
        title_html = f"<strong>{data['job_title']}</strong>"  # Simple hover title, no bullets

        timeline_items.append(
            {
                "id": id_,
                "content": content,
                "start": data["start"],
                "end": data["end"],
                "title": title_html,
                "className": data["className"],
                "type": "point"
                if short_role(data["start"], data["end"], 365)
                else "range",
            }
        )

    return timeline_items


def render_career_snapshot(work_experience: dict):
    with st.container():
        st.subheader("📌 Career Snapshot")
        st.text("Scroll left and right to view my career timeline!")

        options = {
            "stack": True,
            "orientation": "top",
            "zoomable": True,
            "editable": False,
            "margin": {"item": 30, "axis": 20},
            "verticalScroll": True,
            "horizontalScroll": True,
        }
        items = convert_to_timeline_items(work_experience)
        st_timeline(items, options=options, height="750px")
        # Inject styles to prevent item truncation
        st.markdown(
            """
        <style>
        /* Force item and content to expand naturally */
        .vis-item {
            display: inline-flex !important;
            align-items: center;
            white-space: normal !important;
            overflow: visible !important;
            text-overflow: unset !important;
            width: auto !important;
            min-width: fit-content !important;
            max-width: none !important;
            padding: 6px 12px;
            font-size: 14px;
            border-radius: 8px;
            background-color: #64748b !important;
            color: white !important;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }

        .vis-item-content {
            display: block !important;
            white-space: normal !important;
            overflow: visible !important;
            text-overflow: unset !important;
            width: auto !important;
            min-width: fit-content !important;
            max-width: none !important;
        }
        </style>
        """,
            unsafe_allow_html=True,
        )


def format_date(date_str):
    return datetime.strptime(date_str, "%Y-%m-%d").strftime("%b %Y")


def parse_date_or_now(date_str, current=False):
    """Returns a datetime object or a max-future date if 'current' is True"""
    if current:
        return datetime.max
    return datetime.strptime(date_str, "%Y-%m-%d")


def render_work_experience_page(work_experience_dict):
    st.title("💼 Work Experience")

    # Sort jobs by most recent (based on end or 'Present')
    sorted_roles = sorted(
        work_experience_dict.items(),
        key=lambda x: (
            parse_date_or_now(x[1]["end"], x[0] == 1),
            x[1]["start"],
        ),
        reverse=True,
    )

    for role_id, role in sorted_roles:
        job_title = role["job_title"]
        company = role["company"]
        start = format_date(role["start"])
        end = "Present" if role_id == 1 else format_date(role["end"])
        duration = f"{start} — {end}"
        bullets = role["bullets"]
        logo_url = role.get("logo_url", None)

        label = f"{job_title} at {company}"

        with st.expander(label):
            st.markdown(
                f"""
            <div style='display: flex; align-items: center; justify-content: space-between;'>
                <div style='font-size: 16px; font-weight: bold;'>
                    📅 {duration}
                </div>
                <div>
                    <img src="{logo_url}" width="50"/>
                </div>
            </div>
            """,
                unsafe_allow_html=True,
            )

            for bullet in bullets:
                st.markdown(f"- {bullet}")
