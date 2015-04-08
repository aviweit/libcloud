# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
class Provider(object):

# TODO: elaborate more on these specific AWS regions
    """
    Defines for each of the supported providers

    :cvar AWS_AUTOSCALE: Amazon AWS US N. Virgina
    :cvar AWS_AUTOSCALE_US_EAST: Amazon AWS US N. Virgina
    :cvar AWS_AUTOSCALE_EU_WEST: Amazon AWS EU Ireland
    :cvar AWS_AUTOSCALE_US_WEST: Amazon AWS US N. California
    :cvar AWS_AUTOSCALE_US_WEST_OREGON: Amazon AWS US Oregon
    :cvar AWS_AUTOSCALE_AP_SOUTHEAST: Amazon AWS US N. California
    :cvar AWS_AUTOSCALE_US_WEST: Amazon AWS US N. California
    :cvar AWS_AUTOSCALE_US_WEST: Amazon AWS US N. California
    :cvar SOFTLAYER: Softlayer
    """
    AWS_AUTOSCALE = 'aws_autoscale_us_east'
    AWS_CLOUDWATCH = 'aws_cloudwatch_us_east'

    AWS_AUTOSCALE_US_EAST = 'aws_autoscale_us_east'
    AWS_AUTOSCALE_EU_WEST = 'aws_autoscale_eu_west'
    AWS_AUTOSCALE_US_WEST = 'aws_autoscale_us_west'
    AWS_AUTOSCALE_US_WEST_OREGON = 'aws_autoscale_us_west_oregon'
    AWS_AUTOSCALE_AP_SOUTHEAST = 'aws_autoscale_ap_southeast'
    AWS_AUTOSCALE_AP_SOUTHEAST2 = 'aws_autoscale_ap_southeast_2'
    AWS_AUTOSCALE_AP_NORTHEAST = 'aws_autoscale_ap_northeast'
    AWS_AUTOSCALE_SA_EAST = 'aws_autoscale_sa_east'

    AWS_CLOUDWATCH_US_EAST = 'aws_cloudwatch_us_east'
    AWS_CLOUDWATCH_US_WEST = 'aws_cloudwatch_us_west'
    AWS_CLOUDWATCH_US_WEST_OREGON = 'aws_cloudwatch_us_west_oregon'
    AWS_CLOUDWATCH_EU_WEST = 'aws_cloudwatch_eu_west'
    AWS_CLOUDWATCH_AP_SOUTHEAST = 'aws_cloudwatch_ap_southeast'
    AWS_CLOUDWATCH_AP_SOUTHEAST2 = 'aws_cloudwatch_ap_southeast_2'

    SOFTLAYER = 'softlayer'


class AutoScaleAdjustmentType(object):
    """
    The logic to be used to scale the group when its policy is executed.

    :cvar CHANGE_IN_CAPACITY: Increases or decreases the existing capacity.
    :cvar EXACT_CAPACITY: Changes the current capacity to the specified value.
    :cvar PERCENT_CHANGE_IN_CAPACITY: Increases or decreases the capacity by a
                                      percentage.
    """

    CHANGE_IN_CAPACITY = 'CHANGE_IN_CAPACITY'
    EXACT_CAPACITY = 'EXACT_CAPACITY'
    PERCENT_CHANGE_IN_CAPACITY = 'PERCENT_CHANGE_IN_CAPACITY'


class AutoScaleTerminationPolicy(object):
    """
    The policy to be used for automatic removal of members from an auto scale
    group. Policy determines which members are chosen first for removal.

    :cvar OLDEST_INSTANCE: Terminates the oldest instance in the group.
    :cvar NEWEST_INSTANCE: Terminates the newest instance in the group.
    :cvar CLOSEST_TO_NEXT_CHARGE: Terminates instances that are closest to the
    next billing charge.
    :cvar DEFAULT: Default termination policy.

    """
    OLDEST_INSTANCE = 0
    NEWEST_INSTANCE = 1
    CLOSEST_TO_NEXT_CHARGE = 2
    DEFAULT = 3


class AutoScaleOperator(object):
    """
    The arithmetic operation to use when comparing the statistic
    and threshold.

    :cvar LT: Less than.
    :cvar LE: Less equals.
    :cvar GT: Greater than.
    :cvar GE: Great equals.

    """

    LT = 'LT'
    LE = 'LE'
    GT = 'GT'
    GE = 'GE'


class AutoScaleMetric(object):
    """
    :cvar CPU_UTIL: The percent CPU a guest is using.
    """
    CPU_UTIL = 'CPU_UTIL'
