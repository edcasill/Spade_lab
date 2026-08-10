// This is an example of how to do BDI programming

// =================
//     BELIEFS
// =================
// The agent is at the base and his battery is fully charged

location(base).
battery_state(high).

// =================
//     DESIRES
// =================
// When the agent born, it has the desire to monitor his rangers

!start_monitor.

// =================
//     INTENTIONS
// =================
// The plan (+!) he's going to implement to achieve his goal

// Plan A: patrolling with high battery
+!start_monitor : battery_state(high) <-
    .print("Commander: Commander online. Monitoring communications...");

// Secondary desire plan
+need_asistance[source(sender)] <-
    .print("Commander: WARNING, message received from: ", sender).
    .print("Commander: Sending rescue unit").