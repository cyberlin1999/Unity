using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Camera : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {

    }

    // Update is called once per frame
    void Update()
    {
        // Spin the object around the target at 20 degrees/second.
        Vector3 axis = new Vector3(Mathf.Cos(Time.time/10), 0, Mathf.Sin(Time.time/10));
        transform.RotateAround(Vector3.zero, axis, 20 * Time.deltaTime);
    }
}
