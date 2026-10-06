from django.db import migrations


def split_country(apps, schema_editor):
    ExchangeProgram = apps.get_model("faculty", "ExchangeProgram")
    for program in ExchangeProgram.objects.all():
        text = program.university
        if text.endswith(")"):
            name, country = text[:-1].rsplit(" (", 1)
        elif " - " in text:
            name, country = text.rsplit(" - ", 1)
        else:
            name, country = text.rsplit(", ", 1)
        program.university = name
        program.country = country
        program.save(update_fields=["university", "country"])


def join_country(apps, schema_editor):
    # Original separators ("(...)", " - ", ", ") are not stored,
    # so rollback rejoins every row with ", ".
    ExchangeProgram = apps.get_model("faculty", "ExchangeProgram")
    for program in ExchangeProgram.objects.all():
        program.university = f"{program.university}, {program.country}"
        program.country = ""
        program.save(update_fields=["university", "country"])


class Migration(migrations.Migration):
    dependencies = [
        ("faculty", "0004_exchangeprogram_country"),
    ]

    operations = [
        migrations.RunPython(split_country, reverse_code=join_country),
    ]