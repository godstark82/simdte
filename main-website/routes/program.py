# from flask import Blueprint, render_template, current_app
# from services import schedule_service, faq_service, components_service
# program_bp = Blueprint("program", __name__)


# @program_bp.route("/awards-grants")
# def AwardsAndGrants():
#     navItems = components_service.get_navbar_items()
#     rewards = faq_service.get_rewards_grants()
#     components = components_service.get_all_components()
#     return render_template('screens/program/awardsngrants.html', rewards=rewards, website_title=current_app.config['website_title'], navbar_title=current_app.config['navbar_title'], domain=current_app.config['domain'], components=components, navItems=navItems)