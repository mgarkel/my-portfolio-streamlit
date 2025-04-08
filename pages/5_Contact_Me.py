# -----------------  contact  ----------------- #
from components.contact import render_contact_section
from constant import info
from utils.general_utils import local_css, render_sidebar_photo

local_css("style/style.css")
render_sidebar_photo()
render_contact_section(info["Email"])
