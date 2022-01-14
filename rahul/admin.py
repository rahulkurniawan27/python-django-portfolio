from pyexpat import model
from django.contrib import admin
from .models import Home, About, Profile, Category, Skills, Portofolio

# RHome
admin.site.register(Home)


#about
class ProfileInline(admin.TabularInline):
    model = Profile
    extra = 1

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    inlines = [
        ProfileInline
    ]

#skill
class SkillsInline(admin.TabularInline):
    model = Skills
    extra = 2

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        SkillsInline
    ]

#portofolio
admin.site.register(Portofolio)
