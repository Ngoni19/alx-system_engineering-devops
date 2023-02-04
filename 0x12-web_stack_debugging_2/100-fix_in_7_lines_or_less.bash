#!/usr/bin/env bash
# Script runs the nginx server not as super user.
chmod 644 /etc/nginx/nginx.conf
sed -Ei 's/\s*#?\s*user .*/user nginx;/' /etc/nginx/nginx.conf
sed -Ei 's/(listen (\[::\]:)?80) /\180 /' /etc/nginx/sites-enabled/default
pkill apache2
su nginx -s /bin/bash -c