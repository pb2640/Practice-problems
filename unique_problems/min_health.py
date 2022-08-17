class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        return 1+sum(damage)-min(armor,max(damage))