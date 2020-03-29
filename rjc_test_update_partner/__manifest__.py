# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    "name": "RJC test update partner",
    "description": """
Test chagne partner name with URL

http://localhost:8069/update_partner_name/1/NEW_NAME

It will return a string

{'partner_id': 1, 'old_name': 'OLD_NAME', 'new_name': 'NEW_NAME'}
    """,
    "version": "13.0.1.0.0",
    "development_status": "Beta",
    "author": "Kitti U.",
    "depends": ["base"],
    "installable": True,
}
