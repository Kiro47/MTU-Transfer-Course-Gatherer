from django.test import TestCase
from course_gather.models import (
    College,
    Course,
    MTUCourse,
    State
)


class StateTest(TestCase):
    model = State

    def setUp(self):
        self.model.objects.create(state_code='test_code123',
                                  state_name='Test State')

    def tearDown(self):
        self.model.objects.all().delete()

    def test_state_create(self):
        new_state = self.model.objects.create(state_code='new_code321',
                                              state_name='New Test State')
        self.assertEqual(new_state.state_name, 'New Test State')
        self.assertEqual(new_state.state_code, 'new_code321')

    def test_state_read(self):
        state = self.model.objects.get(state_code='test_code123')
        self.assertEqual(state.state_name, 'Test State')

    def test_state_update(self):
        self.model.objects.filter(state_code='test_code123').update(
                                            state_name='Updated State')
        updated_state = self.model.objects.get(state_name='Updated State')
        self.assertEqual(updated_state.state_name, 'Updated State')

    def test_state_destroy(self):
        self.model.objects.get(state_name='Test State').delete()
        states = self.model.objects.all()
        self.assertEqual(len(states), 0)


class CollegeTest(TestCase):
    model = College

    def setUp(self):
        self.model.objects.create(college_code='test_code123',
                                  college_name='Fake College')

    def tearDown(self):
        self.model.objects.all().delete()

    def test_college_create(self):
        new_entry = self.model.objects.create(college_code='new_code321',
                                              college_name='New Test College')
        self.assertEqual(new_entry.college_name, 'New Test College')
        self.assertEqual(new_entry.college_code, 'new_code321')

    def test_college_read(self):
        college = self.model.objects.get(college_code='test_code123')
        self.assertEqual(college.college_name, 'Fake College')

    def test_college_update(self):
        self.model.objects.filter(college_code='test_code123').update(
                                                college_name='Updated College')
        updated_college = self.model.objects.get(
                                                college_name='Updated College')
        self.assertEqual(updated_college.college_name, 'Updated College')

    def test_college_destroy(self):
        self.model.objects.get(college_name='Fake College').delete()
        colleges = self.model.objects.all()
        self.assertEqual(len(colleges), 0)


class MTUCourseTest(TestCase):
    model = MTUCourse

    def setUp(self):
        self.model.objects.create(mtu_course_id='TST1001',
                                  mtu_course_name='Test 101',
                                  mtu_subject='Test',
                                  mtu_credits=3.0)

    def tearDown(self):
        self.model.objects.all().delete()

    def test_mtu_course_create(self):
        pass

    def test_mtu_course_read(self):
        pass

    def test_mtu_course_update(self):
        pass

    def test_mtu_course_destroy(self):
        pass


class CourseTest(TestCase):
    model = Course

    def setUp(self):
        pass

    def tearDown(self):
        self.model.objects.all().delete()

    def test_course_create(self):
        pass

    def test_course_read(self):
        pass

    def test_course_update(self):
        pass

    def test_course_destroy(self):
        pass
