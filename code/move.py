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
    goal_positions =[[0.039, 0.044],
                    [0.130,  1.636],
                    [0.533,  1.636],
                    [0.673,  0.392],
                    [1.221,  0.392],
                    [1.282, 1.939]]

    goal_pose = [[0.670,    0.742],
                 [0.717,    0.698],
                 [0.250,    1.000],
                 [-0.699,   0.716],
                 [0.721,    0.693],
                 [0.693,    0.721]]

    rospy.init_node("set_navigation_goal")

    for x, y in goal_positions & z, w in goal_pose:
        result = move_base_to(x, y, z, w)
        if result:
            continue

            break

        rospy.logininfo("Good job!!!")
