# Generated by Django 3.0.7 on 2021-03-15 11:10

from django.db import migrations, models
import django.db.models.deletion
import problems.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("quizzes", "0001_initial"),
        ("contenttypes", "0002_remove_content_type_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="Problem",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "content_type",
                    models.ForeignKey(
                        limit_choices_to=problems.models.limit_content_type_choices,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="problems",
                        to="contenttypes.ContentType",
                    ),
                ),
                (
                    "quiz",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="problems",
                        to="quizzes.Quiz",
                    ),
                ),
            ],
            options={
                "default_related_name": "problems",
            },
        ),
        migrations.CreateModel(
            name="IskanjeNicelPolinoma",
            fields=[
                (
                    "problem_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="problems.Problem",
                    ),
                ),
                ("stevilo_nicel", models.PositiveSmallIntegerField()),
                ("velikost_nicle", models.PositiveSmallIntegerField()),
            ],
            bases=("problems.problem",),
        ),
        migrations.CreateModel(
            name="KrajsanjeUlomkov",
            fields=[
                (
                    "problem_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="problems.Problem",
                    ),
                ),
                ("najvecji_stevec", models.PositiveSmallIntegerField()),
                ("najvecji_imenovalec", models.PositiveSmallIntegerField()),
                ("najvecji_faktor", models.PositiveSmallIntegerField()),
            ],
            bases=("problems.problem",),
        ),
        migrations.CreateModel(
            name="ProstoBesedilo",
            fields=[
                (
                    "problem_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="problems.Problem",
                    ),
                ),
                ("vprasanje", models.TextField()),
                ("odgovor", models.TextField()),
            ],
            bases=("problems.problem",),
        ),
        migrations.CreateModel(
            name="ProblemText",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("question", models.TextField(blank=True)),
                ("answer", models.TextField(blank=True)),
                (
                    "content_type",
                    models.ForeignKey(
                        limit_choices_to=problems.models.limit_content_type_choices,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="contenttypes.ContentType",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="problem",
            name="text",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="problems",
                to="problems.ProblemText",
            ),
        ),
    ]
