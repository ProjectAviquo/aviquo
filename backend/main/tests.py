from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.test import TestCase

from .models import Opportunity, Tag


class TagTests(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name="scholarship")
        # self.tag.save()

    def test_tag_max_length(self):
        tag = Tag.objects.get(id=1)
        max_length = tag._meta.get_field("name").max_length
        self.assertEquals(max_length, 50)

    def test_tag_max_length_alt(self):
        # Test that name has a maximum length of 50 characters
        tag = Tag(name="X" * 51)
        self.assertRaises(ValidationError, tag.save)

    def test_tag_not_blank(self):
        # Test that name is not blank
        tag = Tag(name="")
        self.assertRaises(Exception, tag.save)

    def test_tag_not_null(self):
        # Test that name is not null
        tag = Tag(name=None)
        self.assertRaises(IntegrityError, tag.save)

    def test_tag_not_unique(self):
        # Test that name is not unique
        with self.assertRaises(IntegrityError):
            Tag.objects.create(name="scholarship")

    def test_tag_not_unique_alt(self):
        tag = Tag(name="scholarship")
        with self.assertRaises(IntegrityError):
            tag.save()

    def test_tag_str_representation(self):
        self.assertEqual(str(self.tag), "scholarship")


class OpportunityTests(TestCase):
    def setUp(self):
        self.opportunity = Opportunity.objects.create(
            name="Test Opportunity",
            description="This is a test opportunity",
        )

    def test_opp_str_representation(self):
        self.assertEqual(str(self.opportunity), "Test Opportunity")

    def test_opp_str_representation_alt(self):
        opportunity = Opportunity(name="An opportunity")
        self.assertEqual(str(opportunity), "An opportunity")

    def test_opp_tags_blank(self):
        self.assertEqual(self.opportunity.tags.count(), 0)

    def test_opp_name_max_length(self):
        # Test that name has a maximum length of 200 characters
        opportunity = Opportunity(name="x" * 201)
        self.assertRaises(Exception, opportunity.save)

    def test_opp_description_max_length(self):
        # Test that description has a maximum length of 4000 characters
        opportunity = Opportunity(description="x" * 4001)
        self.assertRaises(Exception, opportunity.save)

    def test_opp_tags_manytomany(self):
        # Test that tags is a ManyToManyField
        tag1 = Tag.objects.create(name="scholarship")
        tag2 = Tag.objects.create(name="extracurricular activity")
        tag3 = Tag.objects.create(name="internship")
        tag4 = Tag.objects.create(name="job")
        tag5 = Tag.objects.create(name="project")
        tag6 = Tag.objects.create(name="research")
        tag7 = Tag.objects.create(name="volunteer")
        tag8 = Tag.objects.create(name="competition")

        opportunity = Opportunity(name="An opportunity")
        opportunity.save()

        # Test adding tags to opportunity
        opportunity.tags.add(tag1, tag2)
        self.assertEqual(opportunity.tags.count(), 2)
        self.assertIn(tag1, opportunity.tags.all())
        self.assertIn(tag2, opportunity.tags.all())

        # Test removing tag from opportunity
        opportunity.tags.remove(tag2)
        self.assertEqual(opportunity.tags.count(), 1)
        self.assertNotIn(tag2, opportunity.tags.all())

        # Test adding multiple tags at once
        opportunity.tags.add(tag3, tag2)
        self.assertEqual(opportunity.tags.count(), 3)
        self.assertIn(tag2, opportunity.tags.all())
        self.assertIn(tag3, opportunity.tags.all())

        # Test uniqueness of tags associated with opportunity
        opportunity.tags.add(tag3)  # Adding duplicate tag
        self.assertEqual(opportunity.tags.count(), 3)  # Count remains the same
        self.assertIn(tag3, opportunity.tags.all())  # Duplicate tag is still present only once

        # Test uniqueness of tags associated with opportunity
        opportunity.tags.add(tag3)  # Adding duplicate tag
        self.assertEqual(opportunity.tags.count(), 3)  # Count remains the same
        # Count the number of tag3 tags
        tag3_count = opportunity.tags.filter(name="internship").count()
        self.assertEqual(tag3_count, 1)  # Count should be 1

        # Test clearing all tags from opportunity
        opportunity.tags.clear()
        self.assertEqual(opportunity.tags.count(), 0)
        self.assertNotIn(tag1, opportunity.tags.all())
        self.assertNotIn(tag2, opportunity.tags.all())
        self.assertNotIn(tag3, opportunity.tags.all())
