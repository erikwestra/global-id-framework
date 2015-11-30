## global-id-framework ##

This is a Django implementation of the gidframework.com web site.

### The Global ID Framework's API ###

The Global ID Framework includes a simple API for checking if a given name has
been reserved.  To use it, simply access the following URL:

> `/api/is_reserved/xxx`

where `xxx` is the name you want to look up.  The API will return a
JSON-formatted object which looks like the following:

>     {reserved: true}

The `reserved` field will be set to `true` or `false` as appropriate.

More API endpoints will be added in the near future.
