# Nginx web server setup && config
exec { 'apt-get-update':
  command => '/usr/bin/apt-get update',
}

package { 'install nginx':
  ensure  => installed,
  require => Exec['apt-get-update'],
}

file_line { 'redirect me':
  ensure  => 'present',
  path    => '/etc/nginx/sites-available/default',
  after   => 'listen 80 default_server;',
  line    => 'rewrite ^/redirect_me https://google.com permanent;',
  require => Package['nginx'],
}

file_line { 'add header':
  ensure  => 'present',
  path    => '/etc/nginx/sites-available/default',
  after   => 'listen 80 default_server;',
  line    => 'add_header X-Served-By $hostname;',
  require => Package['nginx'],
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
  require => Package['nginx'],
}

service { 'run nginx':
  ensure  => running,
  require => Package['nginx'],
}
