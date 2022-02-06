async def generate_record_text(record_list):
    text = ""
    if record_list["fullName"] is not None and record_list["fullName"] != "":
        text += "<b>" + record_list["fullName"] + "</b>\n"
    if record_list["birthday"] is not None and record_list["birthday"] != "":
        text += "Дата рождения: " + convertDate(record_list["birthday"]) + "\n"
    if record_list["contacts"] is not None and record_list["contacts"] != "":
        text += "Контакты: " + record_list["contacts"] + "\n"
    if record_list["docCountry"] is not None and record_list["docCountry"] != "":
        text += "Страна: " + record_list["docCountry"] + "\n"
    if record_list["docDocument"] is not None and record_list["docDocument"] != "":
        text += "Документ: " + record_list["docDocument"] + "\n"
    if record_list["docCountryActivity"] is not None and record_list["docCountryActivity"] != "":
        text += "ДСА: " + record_list["docCountry"] + "\n"
    if record_list["docSeria"] is not None and record_list["docSeria"] != "":
        text += "Серия: " + record_list["docSeria"] + "\n"
    if record_list["docNumber"] is not None and record_list["docNumber"] != "":
        text += "Номер документа: " + record_list["docNumber"] + "\n"
    if record_list["docDateStart"] is not None and record_list["docDateStart"] != "":
        text += "Выдан: " + record_list["docDateStart"] + "\n"
    if record_list["docDateEnd"] is not None and record_list["docDateEnd"] != "":
        text += "Действителен до: " + record_list["docDateEnd"] + "\n"
    if record_list["docService"] is not None and record_list["docService"] != "":
        text += "Кем выдан: " + record_list["docService"] + "\n"
    if record_list["ipn"] is not None and record_list["ipn"] != "":
        text += "ИНН: " + record_list["ipn"] + "\n"
    if record_list["phone"] is not None and record_list["phone"] != "":
        text += "Телефон: " + record_list["phone"] + "\n"

    return text


def convertDate(date: str):
    new_date = date.split("-")
    return new_date[2] + "." + new_date[1] + "." + new_date[0]
