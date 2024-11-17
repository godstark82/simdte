from flask import Blueprint, render_template, current_app
from services import page_service

about_bp = Blueprint("conferences", __name__)

@about_bp.route("/organizing-committee")
def OrganizingCommittee():
    title = "Organising Committee"
    page = page_service.get_page_content('organising-committee')
    # print(page.content)
    return render_template('screens/about/committee.html', title=title, page=page, 
                           website_title=current_app.config['website_title'], 
                           navbar_title=current_app.config['navbar_title'], 
                           domain=current_app.config['domain'])

@about_bp.route("/scientific-committee")
def ScientificCommittee():
    title = "Scientific Committee"
    page = page_service.get_page_content('scientific-committee-member')
    return render_template('screens/about/committee.html', title=title, page=page, 
                           website_title=current_app.config['website_title'], 
                           navbar_title=current_app.config['navbar_title'], 
                           domain=current_app.config['domain'])

@about_bp.route("/scientific-committe-lead")
def ScientificLead():
    title = "Scientific Lead"
    page = page_service.get_page_content('scientific-lead')
    return render_template('screens/about/committee.html', title=title, page=page, 
                           website_title=current_app.config['website_title'], 
                           navbar_title=current_app.config['navbar_title'], 
                           domain=current_app.config['domain'])