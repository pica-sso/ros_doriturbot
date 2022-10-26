# UTF-8.







import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
PI = 3.14159265359



def move_base_to(x, y):
    client = actionlib.SimpleActionClient("move_base", MoveBaseAction)
    while (not client.wait_for_server(rospy.Duration(5))):
        rospy.loginfo("Waiting for the move_base action server to come up")

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"

    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = x
    goal.target_pose.pose.position.y = y
    if x == 0.0684 and y == 0.0577:
        goal.target_pose.pose.orientation.x = 0.0
        goal.target_pose.pose.orientation.y = 0.0
        goal.target_pose.pose.orientation.z = 0.695
        goal.target_pose.pose.orientation.w = 0.719
    if x == 0.207 and y == 1.635:
        goal.target_pose.pose.orientation.x = 0.0
        goal.target_pose.pose.orientation.y = 0.0
        goal.target_pose.pose.orientation.z = 0.021
        goal.target_pose.pose.orientation.w = 1.000
    if x == 0.533 and y == 1.636:
        goal.target_pose.pose.orientation.x = 0.0
        goal.target_pose.pose.orientation.y = 0.0
        goal.target_pose.pose.orientation.z = 0.250
        goal.target_pose.pose.orientation.w = 1.000
    if x == 0.550 and y == 0.453:
        goal.target_pose.pose.orientation.x = 0.0
        goal.target_pose.pose.orientation.y = 0.0
        goal.target_pose.pose.orientation.z = -0.038
        goal.target_pose.pose.orientation.w = 1.000
    if x == 1.081 and y == 0.427:
        goal.target_pose.pose.orientation.x = 0.0
        goal.target_pose.pose.orientation.y = 0.0
        goal.target_pose.pose.orientation.z = 0.669
        goal.target_pose.pose.orientation.w = 0.743
    if x == 1.221 and y == 1.836:
        goal.target_pose.pose.orientation.x = 0.0
        goal.target_pose.pose.orientation.y = 0.0
        goal.target_pose.pose.orientation.z = 0.672
        goal.target_pose.pose.orientation.w = 0.740
    #goal.target_pose.pose.orientation.x = 0.0
    #goal.target_pose.pose.orientation.y = 0.0
    #goal.target_pose.pose.orientation.z = 0.708
    #goal.target_pose.pose.orientation.w = 1.0
    rospy.loginfo("Sending goal")
    client.send_goal(goal)
    wait = client.wait_for_result()
    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available")
    else:
        return client.get_result()



if __name__ == '__main__':
    goal_positions =[[0.0684, 0.0577],
                    [0.207,  1.635],
                    [0.533,  1.636],
                    [0.550,  0.453],
                    [1.081,  0.427],
                    [1.221, 1.836]]
    rospy.init_node("set_navigation_goal")

    for x, y in goal_positions:
        result = move_base_to(x, y)
        if result:
            continue
        else:
            rospy.loginfo("The move_base failed to get to goal for some reasons")
            break
        rospy.logininfo("Good job!!!")
