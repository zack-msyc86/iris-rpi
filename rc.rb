def rc_exec(command)
  system("python3 ./py/irrp.py -p -g17 -f ./py/codes #{command}")
end

rc_exec(ARGV[0])
