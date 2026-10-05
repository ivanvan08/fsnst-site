from django.db import migrations

INSERT_SQL = """
INSERT INTO faculty_exchangeprogram (university, languages, seats, deadline, description)
VALUES
    ('Uniwersytet Warszawski, Польща', 'польська, англійська', '5', '2026-11-15',
     'Семестр навчання у Варшавському університеті, найбільшому університеті Польщі.'),
    ('KU Leuven (Бельгія)', 'English', '2 місця', '2026-12-01',
     'Семестр у KU Leuven, одному з найстаріших університетів Європи.'),
    ('Vilnius University, Литва', 'англійська', 'до 4', '2026-10-20',
     'Навчання у Вільнюському університеті, найстарішому університеті Литви.'),
    ('Uniwersytet Jagielloński, Польща', 'Польська, Англійська', '3', '2026-11-15',
     'Семестр у Ягеллонському університеті в Кракові.'),
    ('University of Tartu - Естонія', 'англійська, естонська', '2', '2027-01-10',
     'Навчання в Тартуському університеті, головному університеті Естонії.'),
    ('Masaryk University, Чехія', 'англійська', '1 місце', '2026-09-30',
     'Семестр в Університеті Масарика в Брно.');
"""

REVERSE_SQL = """
DELETE FROM faculty_exchangeprogram WHERE university IN (
    'Uniwersytet Warszawski, Польща',
    'KU Leuven (Бельгія)',
    'Vilnius University, Литва',
    'Uniwersytet Jagielloński, Польща',
    'University of Tartu - Естонія',
    'Masaryk University, Чехія'
);
"""


class Migration(migrations.Migration):
    dependencies = [
        ("faculty", "0002_exchangeprogram"),
    ]

    operations = [
        migrations.RunSQL(INSERT_SQL, reverse_sql=REVERSE_SQL),
    ]