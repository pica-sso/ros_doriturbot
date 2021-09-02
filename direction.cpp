#include "ros/ros.h"
#include "string"
#include "sensor_msgs/LaserScan.h"
#include "geometry_msgs/Twist.h"

float front=0; 
float left=0; 
float back=0; 
float right=0;

void msgCallback(const sensor_msgs::LaserScan& msg)
{
    
    front = msg.ranges[0];
    left = msg.ranges[90];
    back = msg.ranges[180];
    right = msg.ranges[270];

    // ROS_INFO("front : %f", front);
    // ROS_INFO("right : %f", right);
    // ROS_INFO("back : %f", back);
    // ROS_INFO("left : %f", left);
    
    ROS_INFO("------------------");

    ROS_INFO("Which Direction ?");
    if(front > 1.0)
        ROS_INFO("FRONT");
    if(right > 1.0)
        ROS_INFO("RIGHT");
    if(back > 1.0)
        ROS_INFO("BACK");
    if(left > 1.0)
        ROS_INFO("LEFT");
    
    ROS_INFO("------------------");        
}

int main(int argc, char**argv)
{
    ros::init(argc, argv, "direction"); // name of node
    ros::NodeHandle nh;

    ros::Publisher turn_cw_pub=nh.advertise<geometry_msgs::Twist>("/cmd_vel",100);

    ros::Subscriber find_dir_sub=nh.subscribe("/scan",100, msgCallback);

    ros::Rate loop_rate(10);

    while(ros::ok())
    {
        geometry_msgs::Twist msg1;
	if (front > 1.0)        
		msg1.linear.x=0.2;
		msg1.linear.y=0.0; 
		msg1.linear.z=0.0;
	    	msg1.angular.x=0.0;
        	msg1.angular.y=0.0;
        	msg1.angular.z=0.0;
	if (front < 1.0)
		msg1.linear.x=0.0;
		msg1.linear.y=0.0; 
		msg1.linear.z=0.0;
	    	msg1.angular.x=0.0;
        	msg1.angular.y=0.0;
        	msg1.angular.z=0.0;
		if (right > 1)
			msg1.linear.x=0.0;
			msg1.linear.y=0.2; 
			msg1.linear.z=0.0;
	    		msg1.angular.x=0.0;
        		msg1.angular.y=0.0;
        		msg1.angular.z=0.0;
			if (left > 1)
				msg1.linear.x=0.0;
				msg1.linear.y=-0.2; 
				msg1.linear.z=0.0;
				msg1.angular.x=0.0;
				msg1.angular.y=0.0;
				msg1.angular.z=0.3;
		if (left > 1)
			msg1.linear.x=0.0;
			msg1.linear.y=-0.2; 
			msg1.linear.z=0.0;
	    		msg1.angular.x=0.0;
        		msg1.angular.y=0.0;
        		msg1.angular.z=0.0;

	//msg1.linear.x=1.0;
        //msg1.linear.y=0.0;
        //msg1.linear.z=0.0;
        //msg1.angular.x=0.0;
        //msg1.angular.y=0.0;
        //msg1.angular.z=0.0;

        turn_cw_pub.publish(msg1);
        ros::spinOnce();
        loop_rate.sleep();
    }

    return 0;
}


		
