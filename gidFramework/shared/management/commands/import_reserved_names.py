""" gidFramework.shared.management.commands.load_reserved_names

    This module implements the "load_reserved_names" management command.  This
    imports the set of reserved names from our "data" directory.
"""
import os.path
import string

from django.conf import settings
from django.core.management.base import BaseCommand,CommandError

from gidFramework.shared.models import *

#############################################################################

class Command(BaseCommand):
    help = "Loads the set of reserved names from the 'data' directory."

    def handle(self, *args, **options):
        """ Run our command.
        """
        while True:
            confirm = input("Replace existing ReservedNames with the " +
                            "contents of the 'data' directory (Y/N)? ")
            if confirm in ['Y', "y", "N", "n"]:
                break

        if confirm in ["N", "n"]:
            return

        reserved_names = {} # Maps name to [twitter_sources, domain_sources]
                            # tuple.

        num_domain_names = 0
        f = open(os.path.join(settings.BASE_DIR, "gidFramework", "shared",
                              "data", "reserved-names-dns.txt"), "r")
        for line in f.readlines():
            line = line.rstrip()
            if len(line) == 0: continue

            name,domains = line.split(" - ", 1)
            domains = domains.split(", ")

            if name in reserved_names:
                reserved_names[name][1].extend(domains)
            else:
                reserved_names[name] = [[], domains]

            num_domain_names = num_domain_names + 1

        print("Imported {} names from DNS".format(num_domain_names))

        num_twitter_names = 0
        f = open(os.path.join(settings.BASE_DIR, "gidFramework", "shared",
                              "data", "reserved-names-twitter.txt"), "r")
        for line in f.readlines():
            line = line.rstrip()
            if len(line) == 0: continue

            screen_name,full_name = line.split("\t", 1)

            name = screen_name.replace("_", "")

            if name in reserved_names:
                reserved_names[name][0].append(screen_name)
            else:
                reserved_names[name] = [[screen_name], []]

            num_twitter_names = num_twitter_names + 1

        print("Imported {} names from Twitter".format(num_twitter_names))

        ReservedName.objects.all().delete()
        reserved_name_recs = []
        for name in reserved_names.keys():
            twitter_sources,domain_sources = reserved_names[name]

            reserved_name = ReservedName()
            reserved_name.name = name

            if len(twitter_sources) > 0:
                reserved_name.twitter_sources = ",".join(twitter_sources)
            else:
                reserved_name.twitter_sources = None

            if len(domain_sources) > 0:
                reserved_name.domain_sources = ",".join(domain_sources)
            else:
                reserved_name.domain_sources = None

            reserved_name_recs.append(reserved_name)

        ReservedName.objects.bulk_create(reserved_name_recs)
        print("Inserted {} ReservedName records".format(
                        len(reserved_name_recs)))

