import { mutation } from 'convex/_generated/server';

// Mutation to schedule a bathroom slot
export default mutation(async ({ db }, { userId }) => {
  // Placeholder AI logic to find an optimal slot
  const optimalSlot = new Date(Date.now() + Math.random() * 60 * 60 * 1000).toISOString();

  // Store the schedule in Convex database
  await db.insert('schedules', {
    userId,
    timeSlot: optimalSlot,
  });

  return optimalSlot;
});
