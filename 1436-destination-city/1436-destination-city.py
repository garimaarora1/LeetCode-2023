class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        source_city_set = set()
        for source_city, destination_city in paths:
            source_city_set.add(source_city)
            
        for _, destination_city in paths:
            if destination_city not in source_city_set:
                return destination_city
        