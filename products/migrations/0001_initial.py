# Generated by Django 4.2.1 on 2023-07-07 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sellers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('en_name', models.CharField(max_length=150, verbose_name='English Name')),
                ('slug', models.SlugField(unique=True, verbose_name='slug')),
            ],
            options={
                'verbose_name': 'Brand',
                'verbose_name_plural': 'Brands',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Title')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
                ('description', models.TextField(verbose_name='Description')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='category_image', verbose_name='Icon')),
                ('image', models.ImageField(blank=True, null=True, upload_to='category_image', verbose_name='ّImage')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.category', verbose_name='Parent Category')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Persian Name')),
                ('en_name', models.CharField(max_length=200, verbose_name='English Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.brand', verbose_name='Brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='products.category', verbose_name='Category')),
            ],
        ),
        migrations.CreateModel(
            name='SellerProductPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField(verbose_name='Price')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='create at')),
                ('update_at', models.DateTimeField(verbose_name='update at')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seller_prices', to='products.product', verbose_name='Product')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sellers.seller', verbose_name='Seller')),
            ],
            options={
                'verbose_name': 'ProductPrice',
                'verbose_name_plural': 'ProductPrices',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Question')),
                ('user_email', models.EmailField(max_length=254, verbose_name='Email')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Question',
                'verbose_name_plural': 'Questions',
            },
        ),
        migrations.CreateModel(
            name='ProductOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('value', models.CharField(max_length=150, verbose_name='Value')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_option', to='products.product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'ProductOption',
                'verbose_name_plural': 'ProductOptions',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='sellers',
            field=models.ManyToManyField(through='products.SellerProductPrice', to='sellers.seller', verbose_name='seller'),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('alt', models.CharField(max_length=50, verbose_name='Alternative Text')),
                ('image', models.ImageField(upload_to='products', verbose_name='Image')),
                ('is_default', models.BooleanField(default=False, verbose_name='Is default image?')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('text', models.TextField(verbose_name='Text')),
                ('rate', models.PositiveSmallIntegerField(verbose_name='Rate')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Answer')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.question', verbose_name='Question')),
            ],
            options={
                'verbose_name': 'Answer',
                'verbose_name_plural': '   Answers',
            },
        ),
    ]
