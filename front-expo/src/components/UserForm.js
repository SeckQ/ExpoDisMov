import React, { useState, useEffect } from 'react';
import axios from 'axios';

const UserForm = ({ user, onUpdate }) => {
  const [formData, setFormData] = useState({
    first_name: '',
    last_name: '',
    birthdate: '',
    nickname: '',
    occupation: '',
    photo: '',
  });

  useEffect(() => {
    if (user) {
      setFormData({
        first_name: user.first_name,
        last_name: user.last_name,
        birthdate: user.birthdate,
        nickname: user.nickname,
        occupation: user.occupation,
        photo: user.photo,
      });
    }
  }, [user]);

  const handleSubmit = event => {
    event.preventDefault();

    const requestMethod = user ? 'put' : 'post';
    const url = user ? `http://localhost:5000/users/${user.id}` : 'http://localhost:5000/users';

    axios[requestMethod](url, formData)
      .then(response => {
        console.log(response.data.message);
        onUpdate();
      })
      .catch(error => console.error(error));
  };

  const handleChange = event => {
    const { name, value } = event.target;
    setFormData(prevState => ({
      ...prevState,
      [name]: value,
    }));
  };

  return (
    <div>
      <h2>{user ? 'Editar Usuario' : 'Crear Nuevo Usuario'}</h2>
      <form onSubmit={handleSubmit}>
        <label>
          First Name:
          <input type="text" name="first_name" value={formData.first_name} onChange={handleChange} />
        </label>
        <br />

        <label>
          Last Name:
          <input type="text" name="last_name" value={formData.last_name} onChange={handleChange} />
        </label>
        <br />

        <label>
          Birthdate:
          <input type="date" name="birthdate" value={formData.birthdate} onChange={handleChange} />
        </label>
        <br />

        <label>
          Nickname:
          <input type="text" name="nickname" value={formData.nickname} onChange={handleChange} />
        </label>
        <br />

        <label>
          Occupation:
          <input type="text" name="occupation" value={formData.occupation} onChange={handleChange} />
        </label>
        <br />

        <label>
          Photo URL:
          <input type="text" name="photo" value={formData.photo} onChange={handleChange} />
        </label>
        <br />

        <button type="submit">{user ? 'Actualizar' : 'Crear Usuario'}</button>
      </form>
    </div>
  );
};

export default UserForm;
