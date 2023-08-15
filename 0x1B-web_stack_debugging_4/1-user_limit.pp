# Change the OS configuration so that it is possible for the Holoberton user to login and open a file without any error messages
exec { 'change soft limit':
	command => 'sudo sed -i "s/holberton\ssoft.*/holberton\tsoft\tnofile\t10000/" /etc/security/limits.conf',
	provider => shell,
}

exec { 'change hard limit':
	command => 'sudo sed -i "s/holberton\shard.*/holberton\thard\tnofile\t100000/" /etc/security/limits.conf',
	provider => shell,
}
