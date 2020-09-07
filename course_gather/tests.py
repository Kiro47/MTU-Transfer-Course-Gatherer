from django.test import TestCase
from course_gather.models import (
    College,
    TransferCourse,
    MTUCourse,
    Location
)


class LocationTest(TestCase):
    model = Location

    def setUp(self):
        self.model.objects.create(location_code='test_code123',
                                  location_name='Test Location')

    def tearDown(self):
        self.model.objects.all().delete()

    def test_create(self):
        new_location = self.model.objects.create(
                                        location_code='new_code321',
                                        location_name='New Test Location')
        self.assertEqual(str(new_location), 'New Test Location')
        self.assertEqual(new_location.location_name, 'New Test Location')
        self.assertEqual(new_location.location_code, 'new_code321')

    def test_location_read(self):
        location = self.model.objects.get(location_code='test_code123')
        self.assertEqual(location.location_name, 'Test Location')

    def test_location_update(self):
        self.model.objects.filter(location_code='test_code123').update(
                                            location_name='Updated Location')
        updated_location = self.model.objects.get(
                                            location_name='Updated Location')
        self.assertEqual(updated_location.location_name, 'Updated Location')

    def test_location_destroy(self):
        self.model.objects.get(location_name='Test Location').delete()
        locations = self.model.objects.all()
        self.assertEqual(len(locations), 0)


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


class TransferCourseTest(TestCase):
    model = TransferCourse
    required_models = [Location, MTUCourse, College]

    def setUp(self):
        Location.objects.create(location_code='test_code123',
                                location_name='Test Location')
        MTUCourse.objects.create(mtu_course_id='TST1001',
                                 mtu_course_name='Test 101',
                                 mtu_subject='Test',
                                 mtu_credits=3.0)
        College.objects.create(college_code='test_code123',
                               college_name='Fake College')

        test_location = Location.objects.get(location_code='test_code123')
        test_college = College.objects.get(college_code='test_code123')
        test_mtu_course = MTUCourse.objects.get(mtu_course_id='TST1001')

        TransferCourse.objects.create(transfer_course_credit=1.0,
                              transfer_course_number='TN101',
                              mtu_equiv=test_mtu_course,
                              transfer_course_college_code=test_college,
                              transfer_course_location_code=test_location)

    def tearDown(self):
        for model in self.required_models:
            model.objects.all().delete()

        self.model.objects.all().delete()

    def test_course_create(self):
        test_location = Location.objects.get(location_code='test_code123')
        test_college = College.objects.get(college_code='test_code123')
        test_mtu_course = MTUCourse.objects.get(mtu_course_id='TST1001')

        test_course = TransferCourse.objects.create(
                                 transfer_course_credit=3.0,
                                 transfer_course_number='TN301',
                                 mtu_equiv=test_mtu_course,
                                 transfer_course_college_code=test_college,
                                 transfer_course_location_code=test_location)

        self.assertEqual(str(test_course), 'TN301')
        self.assertEqual(test_course.transfer_course_credit, 3.0)

    def test_course_read(self):
        course = TransferCourse.objects.get(transfer_course_credit=1.0,
                                    transfer_course_number='TN101')
        self.assertEqual(course.transfer_course_number, 'TN101')
        self.assertEqual(course.transfer_course_credit, 1.0)

    def test_course_update(self):
        TransferCourse.objects.filter(transfer_course_credit=1.0,
                              transfer_course_number='TN101').update(
                              transfer_course_number='TN401',
                              transfer_course_credit=4.0)

        course = TransferCourse.objects.get(transfer_course_credit=4.0,
                                    transfer_course_number='TN401')
        self.assertEqual(course.transfer_course_credit, 4.0)
        self.assertEqual(course.transfer_course_number, 'TN401')

    def test_course_destroy(self):
        self.model.objects.get(transfer_course_number='TN101').delete()
        courses = self.model.objects.all()
        self.assertEqual(len(courses), 0)
