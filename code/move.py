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
    goal_positions_x = [0.357, 0.357, 0.562, 0.9035,0.902,1.1025,1.422,1.4237, 1.5819 ]
    goal_positions_y = [0.777, 0.984, 1.5529, 1.1577,0.7479,0.3192,0.722, 0.927, 1.993]

    goal_pose_z = [0.774, 0.705, 0.02299,-0.7069,-0.7097,-0.000,0.6999, 0.700, 0.698]
    goal_pose_w = [0.633, 0.708, 0.9997, 0.707,0.704,0.9999,0.714, 0.713, 0.715]

    rospy.init_node("set_navigation_goal")

    for x, y, z, w in zip(goal_positions_x, goal_positions_y, goal_pose_z, goal_pose_w):
        result = move_base_to(x, y, z, w)
        if result:
            continue
        elif not result:
            continue
        else:
            break
        rospy.logininfo("Good job!!!")







