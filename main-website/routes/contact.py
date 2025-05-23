from flask import Blueprint, render_template, current_app, request, flash, redirect, url_for
from services import mail_service, components_service

contact_bp = Blueprint("contact", __name__)

@contact_bp.route("/contact", methods=['GET', 'POST'])
def Contact():
    if request.method == 'POST':
        name = request.form.get("name", "")
        email = request.form.get("email", "")
        subject = request.form.get("subject", "")
        message = request.form.get("message", "")

        if not all([name, email, subject, message]):
            flash("Please fill in all fields", "error")
            return redirect(url_for('contact.Contact'))

        mail_service.send_email(name, email, subject, message)
        flash("Message sent successfully", "success")
        return redirect(url_for('contact.Contact'))

    components = components_service.get_all_components()
    navItems = components_service.get_navbar_items()
    return render_template('pages/contact.html', 
        components=components, 
        navItems=navItems)