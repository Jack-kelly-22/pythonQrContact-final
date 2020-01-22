from csv2vcard.export_vcard import check_export, export_vcard
from csv2vcard.create_vcard import create_vcard
from csv2vcard.parse_csv import parse_csv


def csv2vcard(csv_filename: str, csv_delimeter: str):
    """
    Main function
    """
    check_export()

    for c in parse_csv(csv_filename, csv_delimeter):
        vcard = create_vcard(c)
        export_vcard(vcard)


def test_csv2vcard(lastName,firstName,title,phone,email,website):
    """
    Try it out with this mock Forrest Gump contact
    """
    mock_contacts = [{
        "last_name": lastName, "first_name": "Jack", "title": title,
        "org": "room 105",
        "phone": phone, "email": email,
        "website": website,
        "street": "", "city": "", "p_code": "",
        "country": ""
    }]
    check_export()
    vcard = create_vcard(mock_contacts[0])
    return vcard
    #print(vcard)
    export_vcard(vcard)
