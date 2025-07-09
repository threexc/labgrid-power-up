from labgrid import Environment

e = Environment("ecogrid-client.yaml")
t = e.get_target("main")
s = t.get_driver("BeagleplayBootStrategy")
s.transition("shell")
