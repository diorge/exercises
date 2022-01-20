// https://leetcode.com/problems/koko-eating-bananas

object Solution {
  def minEatingSpeed(piles: Array[Int], h: Int): Int = {
    def hoursNeeded(eatingSpeed: Int)(pileSize: Int): BigInt = {
      val q = pileSize / eatingSpeed
      val r = pileSize % eatingSpeed
      if (r != 0) q + 1 else q
    }
    def fastEnough(k: Int): Boolean = {
      piles
        .map(hoursNeeded(k))
        .sum <= h
    }

    // pretty solution but performance problems
    // LazyList.from(1).find(fastEnough).getOrElse(-1)

    // binary search version
    def binSearch(currentMin: Int, currentMax: Int): Int = {
      if (currentMin == currentMax)
        currentMin
      else if (currentMin == currentMax - 1) {
        if (fastEnough(currentMax))
          currentMax
        else
          currentMin
      } else {
        val k = (currentMin + currentMax) / 2
        val fast = fastEnough(k)
        val newMin = if (fast) currentMin else k
        val newMax = if (fast) k else currentMax
        binSearch(newMin, newMax)
      }
    }
    if (fastEnough(1)) 1 else binSearch(1, piles.max)
  }
}
