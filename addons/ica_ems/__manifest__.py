{
    "name":"Education Management System",
    "author":"Agga, IdeaCode Academy",
    "depends":["base","hr","contacts"],
    "data":[
        "security/security_groups.xml",
        "security/ir.model.access.csv",
        # "views/ica_university.xml",
        # "views/ica_department.xml",

        "views/ica_class.xml",
        "views/ica_timetable.xml",
        "views/hr_employee.xml",

        "wizard/ica_booking_wizard.xml",

        "data/ir_sequence.xml",

        "views/menus.xml",
    ],
    "category":"Education",
    "auto_install":False,
    "installable":True,
    "license":"LGPL-3",
}