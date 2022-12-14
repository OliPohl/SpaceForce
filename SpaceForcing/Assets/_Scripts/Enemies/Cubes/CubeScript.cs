using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CubeScript : MonoBehaviour
{
    [SerializeField] private GameSettings GameSettings;
    [SerializeField] private ColorSettings ColorSettings;

    private Rigidbody2D CubeRigidbody;
    private Material CubeMaterial;
    private int Health;
    

    [SerializeField] public bool isBobbing;   // Replace these by GameMaster.
    [SerializeField] public bool isGate;      // Replace these by GameMaster.
    
    void Start()
    {
        CubeRigidbody = GetComponent<Rigidbody2D>();  // Gets the rigidbody of the cube
        CubeMaterial = GetComponent<Renderer>().material;   // Gets the material of the cube
        if (CubeRigidbody == null)
        {
            Debug.LogError("Cube is missing a Rigidbody component");
        }


        if (isGate == true)
        {
            Health = Random.Range(1, GameSettings.GateMaxHealth+1);
        }
        else
        {
            Health = Random.Range(1, GameSettings.CubeMaxHealth+1);
        }
    }

    
    void Update()
    {
        Move();
        UpdateHealth();
        if (isBobbing){Bobbing();}
    }


    private void Move()
    {
        Vector3 TempVect = new Vector3(-1, 0, 0);   // Makes a temp vecotor that will be added to the current positon of the cube. "* Time.deltaTime" makes it so that it it frames(10 frames per CubeSpeed)
        TempVect = TempVect.normalized * Time.deltaTime * GameSettings.CubeSpeed * 7;

        CubeRigidbody.MovePosition(transform.position + TempVect);
    }


    private void Bobbing()
    { 
        
        
        
        
        //ViewPos.y = Mathf.Clamp(ViewPos.y, ((ScreenBounds.y - ObjectHeight) * -1), (ScreenBounds.y - ObjectHeight));
        // Vector3 TempVect = new Vector3(0, -1, 0);
        // TempVect = TempVect.normalized * GameSettings.CubeSpeed * Time.deltaTime;

        // CubeRigidbody.MovePosition(transform.position + TempVect);
    }


    private void UpdateHealth()
    {   
        switch(Health) 
        {
        case 1:
            CubeMaterial.color = ColorSettings.Hp1;
            break;
        case 2:
            CubeMaterial.color = ColorSettings.Hp2;
            break;
        case 3:
            CubeMaterial.color = ColorSettings.Hp3;
            break;
        case 4:
            CubeMaterial.color = ColorSettings.Hp4;
            break;
        case 5:
            CubeMaterial.color = ColorSettings.Hp5;
            break;
        case 6:
            CubeMaterial.color = ColorSettings.Hp6;
            break;
        case 7:
            CubeMaterial.color = ColorSettings.Hp7;
            break;
        case 8:
            CubeMaterial.color = ColorSettings.Hp8;
            break;
        case 9:
            CubeMaterial.color = ColorSettings.Hp9;
            break;
        case 10:
            CubeMaterial.color = ColorSettings.Hp10;
            break;
        default:
            Destroy(gameObject);
            break;
        }
    }


    void OnBecameInvisible() 
    {
        Destroy(gameObject);
    }
}
