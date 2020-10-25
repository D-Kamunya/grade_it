from django.test import TestCase
from .models import Project
from django.contrib.auth.models import User
# Create your tests here.
class ProjectTestClass(TestCase):

    # Set up method
    def setUp(self):
        # Creating a new location and saving it
        self.new_user=User(username='denno',email='a@gmail.com',password='qwerty1234')
        self.new_user.save()
        
        self.new_project= Project(user=self.new_user,title='Pizza Shop',url='https://localhost:8000',description='This ia a django test description',technologies='Django')
        self.new_project.save()



    # Tear Down method
    def tearDown(self):
        Project.objects.all().delete()
        User.objects.all().delete()

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_project,Project))    

    # Testing Save Method
    def test_save_method(self):
        self.new_project1= Project(user=self.new_user,title='Pizza Shop',url='https://localhost:8000',description='This ia a django test description',technologies='Django')
        self.new_project1.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects) == 2)  

    # Testing get all images Method
    def test_get_all_projects_method(self):
        projects = Project.get_all_projects()
        self.assertTrue(len(projects) == 1) 


    # Testing get all images Method
    def test_get_project_by_id_method(self):
        project = Project.get_project_by_id(self.new_project.id)
        self.assertEqual(project.id,self.new_project.id)          


    # Testing delete method
    def test_delete_project(self):
        Project.delete_project(self.new_project.id)
        projects = Project.get_all_projects()
        self.assertTrue(len(projects) == 0)


    # Testing search project by title method
    def test_search_project(self):
        projects=Project.search_project('zza')
        projectss=Project.search_project('Taa')
        self.assertFalse(len(projectss) > 0)  
        self.assertTrue(len(projects) > 0)  


    # Testing filter by userid method
    def test_filter_by_userid(self):
        projects=Project.filter_by_userid(self.new_user.id)
        self.assertTrue(len(projects) > 0)


       
