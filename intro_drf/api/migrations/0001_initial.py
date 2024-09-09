# Generated by Django 5.1 on 2024-09-05 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Institutions',
            fields=[
                ('symbol', models.TextField(blank=True, primary_key=True, serialize=False)),
                ('updated_on', models.TextField(blank=True, null=True)),
                ('net_transaction', models.IntegerField(blank=True, null=True)),
                ('top_sellers', models.JSONField(blank=True, null=True)),
                ('date', models.TextField(blank=True, null=True)),
                ('top_buyers', models.JSONField(blank=True, null=True)),
            ],
            options={
                'db_table': 'institutions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Metadata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sector', models.TextField(blank=True, null=True)),
                ('sub_sector', models.TextField(blank=True, null=True)),
                ('slug', models.TextField(blank=True, null=True)),
                ('sub_sector_id', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'metadata',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Reports',
            fields=[
                ('sub_sector', models.TextField(blank=True, primary_key=True, serialize=False)),
                ('total_companies', models.TextField(blank=True, null=True)),
                ('total_market_cap', models.TextField(blank=True, null=True)),
                ('avg_market_cap', models.TextField(blank=True, null=True)),
                ('filtered_median_pe', models.TextField(blank=True, null=True)),
                ('filtered_weighted_avg_pe', models.TextField(blank=True, null=True)),
                ('min_company_pe', models.TextField(blank=True, null=True)),
                ('max_company_pe', models.TextField(blank=True, null=True)),
                ('avg_yoy_q_earnings_growth', models.TextField(blank=True, null=True)),
                ('avg_yoy_q_revenue_growth', models.TextField(blank=True, null=True)),
                ('weighted_max_drawdown', models.TextField(blank=True, null=True)),
                ('weighted_rsd_close', models.TextField(blank=True, null=True)),
                ('median_yield_ttm', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'reports',
                'managed': False,
            },
        ),
    ]
