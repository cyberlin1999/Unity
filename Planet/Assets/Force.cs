using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Force : MonoBehaviour
{
    public GameObject obj;
    private Rigidbody rb;
    public float C = 10;
    public Vector3 start_impulse;
    // Start is called before the first frame update
    void Start()
    {
        rb = GetComponent<Rigidbody>();
        rb.AddForce(start_impulse, ForceMode.VelocityChange);
    }

    // Update is called once per frame
    void FixedUpdate()
    {
        float distanse = obj.transform.position.magnitude;
        Vector3 cos = obj.transform.position/distanse;
        rb.AddForce(-cos*(C/distanse*distanse));
    }
}
