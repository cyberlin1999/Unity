using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Force1 : MonoBehaviour
{
    public GameObject obj1;
    private Rigidbody rb1;
    public GameObject obj2;
    public GameObject obj3;
    public float C = 10;
    public Vector3 start_velocity1;
    // Start is called before the first frame update
    void Start()
    {
        rb1 = GetComponent<Rigidbody>();
        rb1.AddForce(start_velocity1, ForceMode.VelocityChange);
    }

    // Update is called once per frame
  
    void FixedUpdate()
    {
        Vector3 f1 = obj2.transform.position - obj1.transform.position;
        Vector3 f2 = obj3.transform.position - obj1.transform.position;
        Vector3 cos1 = f1.normalized;
        Vector3 cos2 = f2.normalized;
        rb1.AddForce(cos1*C/(f1.magnitude*f1.magnitude)+ cos2 * C / (f2.magnitude * f2.magnitude), ForceMode.Impulse);
    }
}
