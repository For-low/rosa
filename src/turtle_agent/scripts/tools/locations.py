#  Copyright (c) 2024. Jet Propulsion Laboratory. All rights reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#  https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

"""
Location database for the TurtleSim delivery system.
This stores named locations with their coordinates for navigation.
"""

# Dictionary mapping location names to coordinates (x, y)
locations = {
    "professor_room": (3.0, 3.0),
    "water_point": (4.0, 8.0),
    "laboratory1": (5.0, 9.0),
    "laboratory2": (5.0, 8.0)
}

def get_location_coords(location_name):
    """
    Get coordinates for a named location.
    
    :param location_name: The name of the location
    :return: Tuple of (x, y) coordinates or None if not found
    """
    # Normalize input (remove spaces, lowercase)
    normalized_name = location_name.lower().replace(" ", "_").replace("'", "")
    return locations.get(normalized_name)

def get_all_locations():
    """
    Return all available locations.
    
    :return: List of location names
    """
    return list(locations.keys())

def get_closest_location_by_name(partial_name):
    """
    Find location that best matches a partial name.
    
    :param partial_name: Partial or related location name
    :return: Best matching location name or None
    """
    if not partial_name:
        return None
        
    normalized_query = partial_name.lower().replace(" ", "_").replace("'", "")
    
    # Exact match
    if normalized_query in locations:
        return normalized_query
    
    # Partial match
    for loc in locations.keys():
        if normalized_query in loc:
            return loc
            
    return None 