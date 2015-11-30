from django.db import models

#############################################################################

class ReservedName(models.Model):
    """ A reserved name.

        Reserved names come from one of two possible sources: A registered
        domain name, or a Twitter screen name.  Note that because we strip
        hyphens and underscores from the names, a single reserved name might
        have more than one domain or Twitter screen name as its source; the
        `twitter_sources` and `domain_sources` fields hold a comma-separated
        list of the twitter names, and/or the domain names, that this reserved
        name came from.
    """
    id              = models.AutoField(primary_key=True)
    name            = models.TextField(unique=True)
    twitter_sources = models.TextField(null=True)
    domain_sources  = models.TextField(null=True)

