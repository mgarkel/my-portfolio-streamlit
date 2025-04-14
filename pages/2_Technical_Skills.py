# ----------------- skillset ----------------- #
from components.skills import render_skills_section
from utils.general_utils import local_css, render_sidebar_photo

local_css("style/style.css")
render_sidebar_photo()
render_skills_section()
