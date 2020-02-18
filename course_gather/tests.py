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

    def test_create(self):
        new_state = self.model.objects.create(state_code='new_code321',
                                              state_name='New Test State')
        self.assertEqual(str(new_state), 'New Test State')
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
        self.assertEqual(str(new_entry), 'New Test College')
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
        new_entry = self.model.objects.create(mtu_course_id='TST2001',
                                              mtu_course_name='Test 201',
                                              mtu_subject='Test2',
                                              mtu_credits=0.5)

        self.assertEqual(str(new_entry), 'TST2001')
        self.assertEqual(new_entry.mtu_credits, 0.5)
        self.assertEqual(new_entry.mtu_subject, 'Test2')
        self.assertEqual(new_entry.mtu_course_name, 'Test 201')
        self.assertEqual(new_entry.mtu_course_id, 'TST2001')

    def test_mtu_course_read(self):
        initial_entry = self.model.objects.get(mtu_course_id='TST1001')

        self.assertEqual(initial_entry.mtu_credits, 3.0)
        self.assertEqual(initial_entry.mtu_subject, 'Test')
        self.assertEqual(initial_entry.mtu_course_name, 'Test 101')
        self.assertEqual(initial_entry.mtu_course_id, 'TST1001')

    def test_mtu_course_update(self):
        self.model.objects.filter(mtu_course_id='TST1001').update(
                                                mtu_course_id='TST3001',
                                                mtu_course_name='Test 301',
                                                mtu_subject='Test',
                                                mtu_credits=4.0)

        updated_entry = self.model.objects.get(mtu_course_id='TST3001')

        self.assertEqual(updated_entry.mtu_credits, 4.0)
        self.assertEqual(updated_entry.mtu_subject, 'Test')
        self.assertEqual(updated_entry.mtu_course_name, 'Test 301')
        self.assertEqual(updated_entry.mtu_course_id, 'TST3001')

    def test_mtu_course_destroy(self):
        self.model.objects.get(mtu_course_id='TST1001').delete()
        mtu_courses = self.model.objects.all()
        self.assertEqual(len(mtu_courses), 0)


class CourseTest(TestCase):
    model = Course
    required_models = [State, MTUCourse, College]

    def setUp(self):
        State.objects.create(state_code='test_code123',
                             state_name='Test State')
        MTUCourse.objects.create(mtu_course_id='TST1001',
                                 mtu_course_name='Test 101',
                                 mtu_subject='Test',
                                 mtu_credits=3.0)
        College.objects.create(college_code='test_code123',
                               college_name='Fake College')

        test_state = State.objects.get(state_code='test_code123')
        test_college = College.objects.get(college_code='test_code123')
        test_mtu_course = MTUCourse.objects.get(mtu_course_id='TST1001')

        Course.objects.create(transfer_course_credit=1.0,
                              transfer_course_number='TN101',
                              mtu_equiv=test_mtu_course,
                              transfer_course_college_code=test_college,
                              transfer_course_state_code=test_state)

    def tearDown(self):
        for model in self.required_models:
            model.objects.all().delete()

        self.model.objects.all().delete()

    def test_course_create(self):
        test_state = State.objects.get(state_code='test_code123')
        test_college = College.objects.get(college_code='test_code123')
        test_mtu_course = MTUCourse.objects.get(mtu_course_id='TST1001')

        test_course = Course.objects.create(
                                     transfer_course_credit=3.0,
                                     transfer_course_number='TN301',
                                     mtu_equiv=test_mtu_course,
                                     transfer_course_college_code=test_college,
                                     transfer_course_state_code=test_state)

        self.assertEqual(str(test_course), 'TN301')
        self.assertEqual(test_course.transfer_course_credit, 3.0)

    def test_course_read(self):
        course = Course.objects.get(transfer_course_credit=1.0,
                                    transfer_course_number='TN101')
        self.assertEqual(course.transfer_course_number, 'TN101')
        self.assertEqual(course.transfer_course_credit, 1.0)

    def test_course_update(self):
        Course.objects.filter(transfer_course_credit=1.0,
                              transfer_course_number='TN101').update(
                              transfer_course_number='TN401',
                              transfer_course_credit=4.0)

        course = Course.objects.get(transfer_course_credit=4.0,
                                    transfer_course_number='TN401')
        self.assertEqual(course.transfer_course_credit, 4.0)
        self.assertEqual(course.transfer_course_number, 'TN401')

    def test_course_destroy(self):
        self.model.objects.get(transfer_course_number='TN101').delete()
        courses = self.model.objects.all()
        self.assertEqual(len(courses), 0)
