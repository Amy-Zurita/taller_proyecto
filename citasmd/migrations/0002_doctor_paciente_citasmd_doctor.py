# Generated by Django 4.2.2 on 2023-06-20 03:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('citasmd', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_doctor', models.IntegerField(null=True)),
                ('Doc_nomb', models.CharField(max_length=20, null=True)),
                ('Doc_Apellido', models.CharField(max_length=20, null=True)),
                ('especialidad', models.CharField(max_length=20, null=True)),
                ('Doc_direccion', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_paciente', models.IntegerField(null=True)),
                ('Pac_nomb', models.CharField(max_length=20, null=True)),
                ('Pac_Apellido', models.CharField(max_length=20, null=True)),
                ('Pac_edad', models.IntegerField(null=True)),
                ('correo', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='citasmd',
            name='doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='citasmd.doctor'),
        ),
    ]
