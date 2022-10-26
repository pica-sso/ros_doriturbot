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
    if x == 0.524 and y == 0.026:
        goal.target_pose.pose.orientation.x = 0.0
        goal.target_pose.pose.orientation.y = 0.0
        goal.target_pose.pose.orientation.z = -0.0001
        goal.target_pose.pose.orientation.w = 1.0

    if x == 0.674 and y == -0.092:
        goal.target_pose.pose.orientation.x = 0.0
        goal.target_pose.pose.orientation.y = 0.0
        goal.target_pose.pose.orientation.z = -0.696
        goal.target_pose.pose.orientation.w = 0.718
    if x ==  0.826 and y == -0.319:
        goal.target_pose.pose.orientation.x = 0.0
        goal.target_pose.pose.orientation.y = 0.0
        goal.target_pose.pose.orientation.z = -0.690
        goal.target_pose.pose.orientation.w = 0.724
    if x ==  0.723 and y == -1.634:
        goal.target_pose.pose.orientation.x = 0.0
        goal.target_pose.pose.orientation.y = 0.0
        goal.target_pose.pose.orientation.z = -1.000
        goal.target_pose.pose.orientation.w = 0.023
    if x == 0.325 and y == -1.649:
        goal.target_pose.pose.orientation.x = 0.0
        goal.target_pose.pose.orientation.y = 0.0
        goal.target_pose.pose.orientation.z = 0.745
        goal.target_pose.pose.orientation.w = 0.667
    if x == 0.266 and y == -0.435:
        goal.target_pose.pose.orientation.x = 0.0
        goal.target_pose.pose.orientation.y = 0.0
        goal.target_pose.pose.orientation.z = 1.000
        goal.target_pose.pose.orientation.w = 0.005
    if x == -0.247 and y == -0.476:
        goal.target_pose.pose.orientation.x = 0.0
        goal.target_pose.pose.orientation.y = 0.0
        goal.target_pose.pose.orientation.z = -0.711
        goal.target_pose.pose.orientation.w = 0.703
    if x == -0.210 and y == -2.109:
        goal.target_pose.pose.orientation.x = 0.0
        goal.target_pose.pose.orientation.y = 0.0
        goal.target_pose.pose.orientation.z = -0.690
        goal.target_pose.pose.orientation.w = 0.724
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
    goal_positions =[[0.524, 0.026],
                    [0.674,  -0.092],
                    [0.826, -0.319],
                    [0.723,  -1.634],
                    [0.325,  -1.649],
                    [0.266,  -0.435],
                    [-0.247, -0.476],
                    [-0.210, -2.109]]
    rospy.init_node("set_navigation_goal")

    for x, y in goal_positions:
        result = move_base_to(x, y)
        if result:
            continue
        else:
            rospy.loginfo("The move_base failed to get to goal for some reasons")
            break
        rospy.logininfo("Good job!!!")
