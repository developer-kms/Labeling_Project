
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_middle', models.CharField(max_length=256)),
                ('category_color', models.CharField(max_length=256)),
                ('category_product', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('review_id', models.AutoField(primary_key=True, serialize=False)),
                ('review_number', models.CharField(max_length=256)),
                ('category_product', models.CharField(max_length=256)),
                ('review_content', models.TextField()),
                ('first_status', models.BooleanField()),
                ('second_status', models.BooleanField()),
                ('dummy_status', models.BooleanField()),
                ('first_labeled_id', models.CharField(max_length=256)),
                ('second_labeled_id', models.CharField(max_length=256)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Second_Labeled_Data',
            fields=[
                ('second_labeled_id', models.AutoField(primary_key=True, serialize=False)),
                ('second_labeled_emotion', models.CharField(max_length=256)),
                ('second_labeled_target', models.CharField(max_length=256)),
                ('second_labeled_expression', models.CharField(max_length=256)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category')),
                ('review_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.review')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('result_id', models.AutoField(primary_key=True, serialize=False)),
                ('result_emotion', models.CharField(max_length=256)),
                ('result_target', models.CharField(max_length=256)),
                ('result_expression', models.CharField(max_length=256)),
                ('second_labeled_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.second_labeled_data')),
            ],
        ),
        migrations.CreateModel(
            name='First_Labeled_Data',
            fields=[
                ('first_labeled_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_labeled_emotion', models.CharField(max_length=256)),
                ('first_labeled_target', models.CharField(max_length=256)),
                ('first_labeled_expression', models.CharField(max_length=256)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category')),
                ('review_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.review')),
            ],
        ),
    ]
