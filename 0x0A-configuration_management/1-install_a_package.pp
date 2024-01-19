#!/usr/bin/pup
# Install flask (2.1.0)
package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
# Install python3-pip (22.0.2)
package {'python3-pip':
  ensure   => '22.0.2',
  provider => 'pip3'
}
# Install werkzeug(3.0.1)
package {'werkzeug':
  ensure   => '3.0.1',
  provider => 'pip3'
}
