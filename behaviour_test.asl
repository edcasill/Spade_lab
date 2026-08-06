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
// When the agent born, it has the desire (!goal) to be patrolling

!start_patroll.

// =================
//     INTENTIONS
// =================
// The plan (+!) he's going to implement to achieve his goal

// Plan A: patrolling with high battery
+!start_patroll : battery_state(high) <-
    .print("Battery fully charged. Leaving the base and start patrolling...");
    -location(base);        // the agent is no more at the base
    +location(north_zone);  // the agent is at a new location
    !check_enviroment.      // a new goal arise

// if the agent gets the belief that the baterry is low
+battery_state(low) <-
    .print("Warning: Low battery. I need to recharge").

// Plan B: patrolling with low battery
+!start_patroll : battery_state(low) <-
    .print("Low battery. Can not be patrolling").

// Secondary desire plan
+!check_enviroment <-
    .print("Patrolling area... It is ok").