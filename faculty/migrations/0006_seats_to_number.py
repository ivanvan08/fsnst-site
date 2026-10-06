import re

from django.db import migrations, models


def keep_only_number(apps, schema_editor):
    ExchangeProgram = apps.get_model("faculty", "ExchangeProgram")
    for program in ExchangeProgram.objects.all():
        program.seats = re.search(r"\d+", program.seats).group()
        program.save(update_fields=["seats"])


class Migration(migrations.Migration):
    dependencies = [
        ("faculty", "0005_split_university_country"),
    ]

    operations = [
        # Rollback cannot restore the original wording ("2 місця", "до 4"):
        # the column becomes text again but keeps only the digits.
        migrations.RunPython(keep_only_number, reverse_code=migrations.RunPython.noop),
        migrations.AlterField(
            model_name="exchangeprogram",
            name="seats",
            field=models.PositiveIntegerField(),
        ),
    ]