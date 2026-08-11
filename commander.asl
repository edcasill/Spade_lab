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
    .print("Commander: Commander online. Monitoring communications...").

// Secondary desire plan
// 1. a capital letter indicates a variable
// 2. we can add the exact name of the source # hardcode
// 3. we can evaluate with if. 
//    need_asistance[source(Sender)] : Sender == "ranger@localhost" <-
+need_asistance[source(Sender)] <-
    .print("Commander: WARNING, message received from: ", Sender);
    .print("Commander: Sending rescue unit").