from django.test import TestCase
from django.urls import reverse


class trainTest(TestCase):

    # To check if correct template is rendered and url is accessible by name
    def test_view_home_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'train/index.html')

    def test_view_welcome_correct_template(self):
        response = self.client.get(reverse('welcome'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'welcome.html')

    def test_view_train_between_stations_correct_template(self):
        response = self.client.get(reverse('train_between_stations'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'train/train_between_stations.html')

    def test_view_train_info_correct_template(self):
        response = self.client.get(reverse('train_info'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'train/train_info.html')
