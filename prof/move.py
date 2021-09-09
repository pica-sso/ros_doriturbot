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
    if x == 0.039 and y == 0.044:
        goal.target_pose.pose.orientation.x = 0.0
        goal.target_pose.pose.orientation.y = 0.0
        goal.target_pose.pose.orientation.z = 0.670
        goal.target_pose.pose.orientation.w = 0.742
    if x == 0.130 and y == 1.636:
        goal.target_pose.pose.orientation.x = 0.0
        goal.target_pose.pose.orientation.y = 0.0
        goal.target_pose.pose.orientation.z = 0.717
        goal.target_pose.pose.orientation.w = 0.698
    if x == 0.533 and y == 1.636:
        goal.target_pose.pose.orientation.x = 0.0
        goal.target_pose.pose.orientation.y = 0.0
        goal.target_pose.pose.orientation.z = 0.250
        goal.target_pose.pose.orientation.w = 1.000
    if x == 0.673 and y == 0.392:
        goal.target_pose.pose.orientation.x = 0.0
        goal.target_pose.pose.orientation.y = 0.0
        goal.target_pose.pose.orientation.z = -0.699
        goal.target_pose.pose.orientation.w = 0.716
    if x == 1.221 and y == 0.392:
        goal.target_pose.pose.orientation.x = 0.0
        goal.target_pose.pose.orientation.y = 0.0
        goal.target_pose.pose.orientation.z = 0.721
        goal.target_pose.pose.orientation.w = 0.693
    if x == 1.282 and y == 1.939:
        goal.target_pose.pose.orientation.x = 0.0
        goal.target_pose.pose.orientation.y = 0.0
        goal.target_pose.pose.orientation.z = 0.693
        goal.target_pose.pose.orientation.w = 0.721
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
    goal_positions =[[0.039, 0.044],
                    [0.130,  1.636],
                    [0.533,  1.636],
                    [0.673,  0.392],
                    [1.221,  0.392],
                    [1.282, 1.939]]
    rospy.init_node("set_navigation_goal")

    for x, y in goal_positions:
        result = move_base_to(x, y)
        if result:
            continue
        else:
            rospy.loginfo("The move_base failed to get to goal for some reasons")
            break
        rospy.logininfo("Good job!!!")
