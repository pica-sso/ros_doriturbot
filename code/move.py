# UTF-8.







import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
PI = 3.14159265359




def move_base_to(x, y, z, w):
    client = actionlib.SimpleActionClient("move_base", MoveBaseAction)
    while (not client.wait_for_server(rospy.Duration(5))):
        rospy.loginfo("Waiting for the move_base action server to come up")

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"

    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = x
    goal.target_pose.pose.position.y = y
    goal.target_pose.pose.orientation.z = z
    goal.target_pose.pose.orientation.w = w

    rospy.loginfo("Sending goal")
    client.send_goal(goal)
    wait = client.wait_for_result()
    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available")
    else:
        return client.get_result()



if __name__ == '__main__':
    goal_positions_x = [0.039, 0.130, 0.533, 0.673, 1.221, 1.282]
    goal_positions_y = [0.044, 1.636, 1.636, 0.392, 0.392, 1.939]

    goal_pose_z = [0.670, 0.717, 0.250, -0.699, 0.721, 0.693]
    goal_pose_w = [ 0.742,  0.698, 1.000, 0.716, 0.693, 0.721]

    rospy.init_node("set_navigation_goal")

    for x, y, z, w in zip(goal_positions_x, goal_positions_y, goal_pose_z, goal_pose_w):
        result = move_base_to(x, y, z, w)
        if result:
            continue

            break

        rospy.logininfo("Good job!!!")







