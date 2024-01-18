import React, { useState, useEffect } from 'react';
import axios from 'axios';
import UserForm from './UserForm';

const UserList = () => {
  const [users, setUsers] = useState([]);
  const [selectedUser, setSelectedUser] = useState(null);

  useEffect(() => {
    axios.get('http://localhost:5000/users')
      .then(response => setUsers(response.data.users))
      .catch(error => console.error(error));
  }, []);

  const handleEdit = user => {
    setSelectedUser(user);
  };

  const handleDelete = userId => {
    console.log(`Eliminar usuario con ID ${userId}`);
    
    axios.delete(`http://localhost:5000/users/${userId}`)
      .then(response => {
        console.log(response.data.message);
        setUsers(prevUsers => prevUsers.filter(user => user.id !== userId));
      })
      .catch(error => console.error(error));
  };

  return (
    <div>
      <h2>Lista de Usuarios</h2>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>First Name</th>
            <th>Last Name</th>
            <th>Birthdate</th>
            <th>Nickname</th>
            <th>Occupation</th>
            <th>Photo</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          {users.map(user => (
            <tr key={user.id}>
              <td>{user.id}</td>
              <td>{user.first_name}</td>
              <td>{user.last_name}</td>
              <td>{user.birthdate}</td>
              <td>{user.nickname}</td>
              <td>{user.occupation}</td>
              <td>{user.photo}</td>
              <td>
                <button onClick={() => handleEdit(user)}>Editar</button>
                <button onClick={() => handleDelete(user.id)}>Eliminar</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>

      {selectedUser && (
        <UserForm
          user={selectedUser}
          onUpdate={() => {
            setSelectedUser(null);
          }}
        />
      )}
    </div>
  );
};

export default UserList;
